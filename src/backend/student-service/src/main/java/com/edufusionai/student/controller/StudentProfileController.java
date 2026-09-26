package com.campusiq.student.controller;

import com.campusiq.student.entity.StudentProfile;
import com.campusiq.student.repository.StudentProfileRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/student")
public class StudentProfileController {

    @Autowired
    private StudentProfileRepository studentProfileRepository;

    @GetMapping("/profile")
    public ResponseEntity<StudentProfile> getProfile(Authentication authentication) {
        Long userId = extractUserId(authentication);
        StudentProfile profile = studentProfileRepository.findByUserId(userId)
                .orElseGet(() -> {
                    StudentProfile newProfile = StudentProfile.builder()
                            .userId(userId)
                            .major("Undeclared")
                            .enrollmentYear(2026)
                            .gpa(0.0)
                            .build();
                    return studentProfileRepository.save(newProfile);
                });
        return ResponseEntity.ok(profile);
    }

    @PutMapping("/profile")
    public ResponseEntity<StudentProfile> updateProfile(Authentication authentication, @RequestBody StudentProfile updatedProfile) {
        Long userId = extractUserId(authentication);
        StudentProfile profile = studentProfileRepository.findByUserId(userId)
                .orElseThrow(() -> new RuntimeException("Profile not found"));
        
        profile.setMajor(updatedProfile.getMajor());
        profile.setEnrollmentYear(updatedProfile.getEnrollmentYear());
        profile.setGpa(updatedProfile.getGpa());

        return ResponseEntity.ok(studentProfileRepository.save(profile));
    }

    private Long extractUserId(Authentication authentication) {
        // The JwtFilter sets the principal as a Long (userId)
        return Long.parseLong(authentication.getPrincipal().toString());
    }
}
