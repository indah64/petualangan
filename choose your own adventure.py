# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:27:22 2022

@author: asus
"""

nama = input("masukkan nama anda: ")
print("selamat datang", nama, "untuk petualangan yang menyenangkan ini!")

pertanyaan = input(
    "anda sedang berdiri di tengah hutan yang rimba,itu akan bahaya dan ada dua pilihan jalan anda dapat pergi ke kiri atau kanan. jalan mana yang anda pilih? ").lower()

if pertanyaan == "kiri":
    pertanyaan = input("Anda datang ke sebuah danau , anda bisa jalan di sekitar danau nya atau bisa saja berenang? ketik jalan untuk berjalan jalan di sekitar nya dan berenang untuk menyebrang: ")
    
    if pertanyaan == "berenang":
        print("anda berenang menyebrang dan ternyata danau tersebut dalam jadi anda tenggelam .")
    elif pertanyaan == "jalan":
        print("anda berjalan sangat jauh untuk keluar dari hutan, itu membuat lelah dan membuat stok air cepat habis dan anda kalah dalam permainan.")
    else:
        print('bukan pilihan yang valid. kamu kalah.')
        
if pertanyaan == "baiklah":
    pertanyaan = input("anda datang ke jembatan, terlihat lapuk bahkan bisa saja roboh, anda berpikir sejenak untuk menyebrang atau kembali(menyebrang/kembali)? ")
    
    if pertanyaan == "kembali":
        print("anda kembali dan kalah")
    elif pertanyaan == "menyebrang":
        pertanyaan = input ("anda menyebrangi jembatan itu dan bertemu dengan beberapa kera.apakah anda berbicara kepada mereka supaya tidak di ganggu (ya/tidak)? ")
        
    if pertanyaan == "ya":
        print("anda berbicara kepada mereka dan memberi beberapa pisang anda menang!")
    elif pertanyaan == "tidak":
        print("anda mengabaikan kera tersebut hingga membuat nya tersinggung anda kalah.")
    else:
        print('bukan pilihan yang valid, kamu kalah.')
else:
        print('bukan pilihan yang valid. kamu kalah.')
print("terimakasih sudah mencoba petualangan ini", nama)
        
    