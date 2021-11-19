package com.example.timeattack1112.controller;

import com.example.timeattack1112.domain.Memo;
import com.example.timeattack1112.dto.MemoRequestDto;
import com.example.timeattack1112.service.MemoService;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class MemoController {

    private final MemoService memoService;

    @GetMapping("/api/memos/{id}")
    public Memo getMemos(@PathVariable Long id){
        return memoService.getMemos(id);
    }

    @PostMapping("/api/memos")
    public Memo createMemo(@RequestBody MemoRequestDto requestDto){
        Memo memo = memoService.createMemo(requestDto);
        return memo;
    }
}
