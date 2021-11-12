package com.example.timeattack1112.service;

import com.example.timeattack1112.domain.Memo;
import com.example.timeattack1112.dto.MemoRequestDto;
import com.example.timeattack1112.repository.MemoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class MemoService {

    private final MemoRepository memoRepository;

    @Autowired
    public MemoService(MemoRepository memoRepository){
        this.memoRepository=memoRepository;
    }

    public List<Memo> getMemos(){
        return memoRepository.findAll();
    }

    @Transactional
    public Memo createMemo(MemoRequestDto requestDto){
        Memo memo = new Memo(requestDto);
        memoRepository.save(memo);
        return memo;
    }
}
