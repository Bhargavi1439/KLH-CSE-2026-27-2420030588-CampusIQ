package com.campusiq.infrastructure.controller;

import com.campusiq.infrastructure.entity.Infrastructure;
import com.campusiq.infrastructure.repository.InfrastructureRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/infrastructure/requests")
public class InfrastructureController {

    @Autowired
    private InfrastructureRepository infrastructureRepository;

    @GetMapping
    public ResponseEntity<List<Infrastructure>> getAllRequests() {
        return ResponseEntity.ok(infrastructureRepository.findAll());
    }

    @PostMapping
    public ResponseEntity<Infrastructure> createRequest(@RequestBody Infrastructure infrastructure) {
        return ResponseEntity.ok(infrastructureRepository.save(infrastructure));
    }
}
