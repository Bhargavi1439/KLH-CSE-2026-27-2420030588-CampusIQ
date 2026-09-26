package com.campusiq.attendance.entity;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;

@Entity
@Table(name = "attendance_records")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Attendance {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private Long studentId; // User ID of the student

    @Column(nullable = false)
    private Long courseId;  // ID of the course

    @Column(nullable = false)
    private LocalDate date;

    @Column(nullable = false)
    private String status;  // e.g. PRESENT, ABSENT, LATE

}
