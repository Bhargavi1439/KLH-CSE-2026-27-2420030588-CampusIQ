import os
import shutil

base = r'C:\Users\krish\.gemini\antigravity-ide\scratch\CampusIQ-AI\backend'
src_dir = os.path.join(base, 'classroom-service')
dst_dir = os.path.join(base, 'api-gateway')

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)

# Clean up
shutil.rmtree(os.path.join(dst_dir, 'target'), ignore_errors=True)
src_main_java = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'classroom')
shutil.rmtree(os.path.join(src_main_java, 'controller'), ignore_errors=True)
shutil.rmtree(os.path.join(src_main_java, 'entity'), ignore_errors=True)
shutil.rmtree(os.path.join(src_main_java, 'exception'), ignore_errors=True)
shutil.rmtree(os.path.join(src_main_java, 'repository'), ignore_errors=True)
shutil.rmtree(os.path.join(src_main_java, 'security'), ignore_errors=True)

# Rename package
old_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'classroom')
new_pkg = os.path.join(dst_dir, 'src', 'main', 'java', 'com', 'campusiq', 'apigateway')
os.rename(old_pkg, new_pkg)

# Rename Application class
old_app = os.path.join(new_pkg, 'ClassroomServiceApplication.java')
new_app = os.path.join(new_pkg, 'ApiGatewayApplication.java')
os.rename(old_app, new_app)

with open(new_app, 'w', encoding='utf-8') as f:
    f.write('''package com.campusiq.apigateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ApiGatewayApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }

}
''')

# Create a clean pom.xml
pom_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.campusiq</groupId>
        <artifactId>backend</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
    <artifactId>api-gateway</artifactId>
    <name>CampusIQ API Gateway</name>
    <description>API Gateway for CampusIQ</description>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>2023.0.3</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
'''
with open(os.path.join(dst_dir, 'pom.xml'), 'w', encoding='utf-8') as f:
    f.write(pom_xml)

# Create a clean application.yml
app_yml = '''server:
  port: 8080

spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        - id: auth-service
          uri: http://localhost:8081
          predicates:
            - Path=/auth/**
        - id: student-service
          uri: http://localhost:8082
          predicates:
            - Path=/students/**
        - id: faculty-service
          uri: http://localhost:8083
          predicates:
            - Path=/faculty/**
        - id: academic-service
          uri: http://localhost:8084
          predicates:
            - Path=/academic/**
        - id: classroom-service
          uri: http://localhost:8085
          predicates:
            - Path=/classroom/**
        - id: attendance-service
          uri: http://localhost:8086
          predicates:
            - Path=/attendance/**
        - id: resource-service
          uri: http://localhost:8087
          predicates:
            - Path=/resources/**
        - id: transport-service
          uri: http://localhost:8088
          predicates:
            - Path=/transport/**
        - id: event-service
          uri: http://localhost:8089
          predicates:
            - Path=/event/**
        - id: infrastructure-service
          uri: http://localhost:8090
          predicates:
            - Path=/infrastructure/**
        - id: notification-service
          uri: http://localhost:8091
          predicates:
            - Path=/notification/**
      globalcors:
        corsConfigurations:
          '[/**]':
            allowedOrigins: "*"
            allowedMethods:
              - GET
              - POST
              - PUT
              - DELETE
              - OPTIONS
            allowedHeaders: "*"
'''
with open(os.path.join(dst_dir, 'src', 'main', 'resources', 'application.yml'), 'w', encoding='utf-8') as f:
    f.write(app_yml)

# Edit parent pom.xml
parent_pom = os.path.join(base, 'pom.xml')
with open(parent_pom, 'r', encoding='utf-8') as file:
    content = file.read()
if '<module>api-gateway</module>' not in content:
    content = content.replace('<module>notification-service</module>', '<module>notification-service</module>\n        <module>api-gateway</module>')
    with open(parent_pom, 'w', encoding='utf-8') as file:
        file.write(content)
