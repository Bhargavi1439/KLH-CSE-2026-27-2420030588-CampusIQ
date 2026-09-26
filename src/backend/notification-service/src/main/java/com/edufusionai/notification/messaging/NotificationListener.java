package com.campusiq.notification.messaging;

import com.campusiq.notification.config.KafkaTopicConfig;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class NotificationListener {

    @KafkaListener(topics = KafkaTopicConfig.NOTIFICATION_TOPIC, groupId = "notification-group")
    public void receiveMessage(String message) {
        System.out.println("Received message from Kafka: " + message);
        // Here we could parse the message and send an email/sms.
    }
}
