package com.campusiq.attendance.controller;

import com.campusiq.attendance.entity.Attendance;
import com.campusiq.attendance.repository.AttendanceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/attendance/records")
public class AttendanceController {

    @Autowired
    private AttendanceRepository attendanceRepository;

    @GetMapping
    public ResponseEntity<List<Attendance>> getAllRecords() {
        return ResponseEntity.ok(attendanceRepository.findAll());
    }

    @PostMapping
    public ResponseEntity<Attendance> markAttendance(@RequestBody Attendance attendance) {
        return ResponseEntity.ok(attendanceRepository.save(attendance));
    }
}
