package com.campusiq.infrastructure.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "maintenance_requests")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Infrastructure {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String buildingName;

    @Column(nullable = false)
    private String issueDescription;

    @Column(nullable = false)
    private String status; // e.g. PENDING, IN_PROGRESS, RESOLVED

}
