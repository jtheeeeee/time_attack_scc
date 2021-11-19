package com.example.timeattack1112;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@SpringBootApplication
@EnableJpaAuditing
public class TimeAttack1112Application {

    public static void main(String[] args) {
        SpringApplication.run(TimeAttack1112Application.class, args);
    }

}
