package com.campusiq.transport.controller;

import com.campusiq.transport.entity.Transport;
import com.campusiq.transport.repository.TransportRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/transport/routes")
public class TransportController {

    @Autowired
    private TransportRepository transportRepository;

    @GetMapping
    public ResponseEntity<List<Transport>> getAllRoutes() {
        return ResponseEntity.ok(transportRepository.findAll());
    }

    @PostMapping
    public ResponseEntity<Transport> createRoute(@RequestBody Transport transport) {
        return ResponseEntity.ok(transportRepository.save(transport));
    }
}
