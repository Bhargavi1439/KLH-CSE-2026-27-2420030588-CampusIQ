package com.campusiq.dashboard.security;

import com.campusiq.dashboard.entity.Role;
import com.campusiq.dashboard.entity.User;
import com.campusiq.dashboard.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.List;

@Component
@RequiredArgsConstructor
public class DataSeeder implements CommandLineRunner {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public void run(String... args) throws Exception {
        String defaultPassword = passwordEncoder.encode("password123");

        if (!userRepository.existsByEmail("admin@campusiq.edu")) {
            userRepository.save(User.builder()
                    .name("Admin User").email("admin@campusiq.edu").password(defaultPassword).role(Role.ADMIN).active(true).build());
        }
        if (!userRepository.existsByEmail("faculty@campusiq.edu")) {
            userRepository.save(User.builder()
                    .name("Faculty Member").email("faculty@campusiq.edu").password(defaultPassword).role(Role.FACULTY).active(true).build());
        }
        if (!userRepository.existsByEmail("student@campusiq.edu")) {
            userRepository.save(User.builder()
                    .name("Student User").email("student@campusiq.edu").password(defaultPassword).role(Role.STUDENT).active(true).build());
        }
        if (!userRepository.existsByEmail("parent@campusiq.edu")) {
            userRepository.save(User.builder()
                    .name("Parent User").email("parent@campusiq.edu").password(defaultPassword).role(Role.OTHER).active(true).build());
        }
        System.out.println("Seeded missing default users.");
    }
}
