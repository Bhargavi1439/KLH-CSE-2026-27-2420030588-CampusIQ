package com.campusiq.dashboard.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
import java.util.HashMap;

@RestController
@RequestMapping("/dashboard")
public class DashboardController {

    @GetMapping("/student")
    @PreAuthorize("hasRole('STUDENT')")
    public ResponseEntity<Map<String, Object>> getStudentDashboard() {
        Map<String, Object> data = new HashMap<>();
        data.put("role", "STUDENT");
        data.put("overallAttendance", "78%");
        data.put("averageMarks", "82%");
        data.put("predictedScore", "82%");
        data.put("academicRisk", "GOOD");
        data.put("nextClass", "Database Management - 10:00 AM Room C204");
        data.put("aiInsight", "Your attendance in Operating Systems is 68%. Attend the next 4 classes to reach approximately 75%.");
        return ResponseEntity.ok(data);
    }

    @GetMapping("/faculty")
    @PreAuthorize("hasRole('FACULTY')")
    public ResponseEntity<Map<String, Object>> getFacultyDashboard() {
        Map<String, Object> data = new HashMap<>();
        data.put("role", "FACULTY");
        data.put("todaysClasses", 4);
        data.put("assignedStudents", 128);
        data.put("attendanceSummary", "82%");
        data.put("atRiskStudents", 12);
        data.put("pendingTasks", 3);
        data.put("leaveBalance", 12);
        return ResponseEntity.ok(data);
    }

    @GetMapping("/hod")
    @PreAuthorize("hasRole('HOD')")
    public ResponseEntity<Map<String, Object>> getHodDashboard() {
        Map<String, Object> data = new HashMap<>();
        data.put("role", "HOD");
        data.put("departmentStudents", 450);
        data.put("departmentFaculty", 32);
        data.put("averageAttendance", "81%");
        data.put("atRiskStudents", 27);
        data.put("pendingEvents", 5);
        data.put("resourceRequests", 8);
        data.put("facultyLeaveAlerts", 3);
        return ResponseEntity.ok(data);
    }

    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Map<String, Object>> getAdminDashboard() {
        Map<String, Object> data = new HashMap<>();
        data.put("role", "ADMIN");
        data.put("totalStudents", 5000);
        data.put("totalFaculty", 300);
        data.put("totalHods", 15);
        data.put("totalParents", 4500);
        data.put("activeEvents", 12);
        data.put("infrastructureAlerts", 2);
        return ResponseEntity.ok(data);
    }

    @GetMapping("/parent")
    @PreAuthorize("hasRole('PARENT')")
    public ResponseEntity<Map<String, Object>> getParentDashboard() {
        Map<String, Object> data = new HashMap<>();
        data.put("role", "PARENT");
        data.put("childName", "John Doe");
        data.put("attendance", "78%");
        data.put("predictedScore", "82%");
        data.put("academicRisk", "GOOD");
        data.put("upcomingExam", "Database Management Exam - September 10");
        return ResponseEntity.ok(data);
    }
}
