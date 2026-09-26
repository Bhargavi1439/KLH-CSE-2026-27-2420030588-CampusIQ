package com.campusiq.event.messaging;

import com.campusiq.event.config.KafkaTopicConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class EventPublisher {

    @Autowired(required = false)
    private KafkaTemplate<String, String> kafkaTemplate;

    public void publishEvent(String message) {
        if (kafkaTemplate != null) {
            kafkaTemplate.send(KafkaTopicConfig.NOTIFICATION_TOPIC, message);
            System.out.println("Published message to Kafka: " + message);
        } else {
            System.out.println("Kafka is disabled. Message not sent: " + message);
        }
    }
}
