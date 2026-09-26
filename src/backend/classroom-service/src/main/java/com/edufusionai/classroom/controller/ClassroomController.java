package com.campusiq.classroom.controller;

import com.campusiq.classroom.entity.Classroom;
import com.campusiq.classroom.repository.ClassroomRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/classroom/rooms")
public class ClassroomController {

    @Autowired
    private ClassroomRepository classroomRepository;

    @GetMapping
    public ResponseEntity<List<Classroom>> getAllClassrooms() {
        return ResponseEntity.ok(classroomRepository.findAll());
    }

    @PostMapping
    public ResponseEntity<Classroom> createClassroom(@RequestBody Classroom classroom) {
        return ResponseEntity.ok(classroomRepository.save(classroom));
    }
}
