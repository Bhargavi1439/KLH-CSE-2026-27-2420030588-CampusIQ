package com.campusiq.student.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "student_profiles")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class StudentProfile {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // Links to auth_service users.id
    @Column(nullable = false, unique = true)
    private Long userId;

    @Column(nullable = false)
    private String major;

    @Column(nullable = false)
    private Integer enrollmentYear;

    private Double gpa;

}
