package com.campusiq.faculty.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "faculty_profiles")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class FacultyProfile {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // Links to auth_service users.id
    @Column(nullable = false, unique = true)
    private Long userId;

    @Column(nullable = false)
    private String department;

    @Column(nullable = false)
    private String title;

    private String officeLocation;

}
