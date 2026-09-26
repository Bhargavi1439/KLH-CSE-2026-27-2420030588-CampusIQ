FROM maven:3.9.6-eclipse-temurin-21-alpine
WORKDIR /app
ARG SERVICE_NAME=auth-service
ENV SERVICE_NAME=${SERVICE_NAME}

COPY . .

RUN mvn clean package -DskipTests -pl ${SERVICE_NAME} -am
CMD java -jar /app/${SERVICE_NAME}/target/${SERVICE_NAME}-1.0.0-SNAPSHOT.jar
