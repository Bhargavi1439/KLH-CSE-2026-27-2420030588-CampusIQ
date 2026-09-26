package com.campusiq.faculty.controller;

import com.campusiq.faculty.entity.FacultyProfile;
import com.campusiq.faculty.repository.FacultyProfileRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/faculty")
public class FacultyProfileController {

    @Autowired
    private FacultyProfileRepository facultyProfileRepository;

    @GetMapping("/profile")
    public ResponseEntity<FacultyProfile> getProfile(Authentication authentication) {
        Long userId = extractUserId(authentication);
        FacultyProfile profile = facultyProfileRepository.findByUserId(userId)
                .orElseGet(() -> {
                    FacultyProfile newProfile = FacultyProfile.builder()
                            .userId(userId)
                            .department("General")
                            .title("Professor")
                            .officeLocation("TBD")
                            .build();
                    return facultyProfileRepository.save(newProfile);
                });
        return ResponseEntity.ok(profile);
    }

    @PutMapping("/profile")
    public ResponseEntity<FacultyProfile> updateProfile(Authentication authentication, @RequestBody FacultyProfile updatedProfile) {
        Long userId = extractUserId(authentication);
        FacultyProfile profile = facultyProfileRepository.findByUserId(userId)
                .orElseThrow(() -> new RuntimeException("Profile not found"));
        
        profile.setDepartment(updatedProfile.getDepartment());
        profile.setTitle(updatedProfile.getTitle());
        profile.setOfficeLocation(updatedProfile.getOfficeLocation());

        return ResponseEntity.ok(facultyProfileRepository.save(profile));
    }

    private Long extractUserId(Authentication authentication) {
        return Long.parseLong(authentication.getPrincipal().toString());
    }
}
