10 CLS: PRINT @ 412,"AMAZING"
20 PRINT @ 538,"COPYRIGHT BY"
30 PRINT @ 587,"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY"
40 FOR II=1 TO 1500: NEXT
50 CLS: INPUT"WHAT ARE YOUR WIDTH AND LENGTH"; H,V
60 IF H<>1 AND V<>1 THEN 90
70 PRINT "MEANINGLESS DIMENSIONS. TRY AGAIN"
80 FOR A=1 TO 500: NEXT A: GOTO 50
90 PRINT @ 522,"PRINTOUT IS IN PROGRESS, PLEASE BE PATIENT";
100 FOR II=1 TO 1500: NEXT
110 DIM W(H,V), V(H,V)
120 Q=0: Z=0: X=RND(H)
130 FOR I=1 TO H
140 IF I=X THEN 160
150 LPRINT ":--";: GOTO 170
160 LPRINT ":  ";
170 NEXT I
180 LPRINT ":"
190 C=1: W(X,1)=C: C=C+1
200 R=X: S=1: GOTO 270
210 IF R<>H THEN 250
220 IF S<>V THEN 240
230 R=1: S=1: GOTO 260
240 R=1: S=S+1: GOTO 260
250 R=R+1
260 IF W(R,S)=0 THEN 210
270 IF R-1=0 THEN 600
280 IF W(R-1,S) <>0 THEN 600
290 IF S-1=0 THEN 430
300 IF W(R,S-1)<>0 THEN 430
310 IF R=H THEN 350
320 IF W(R+1,S)<>0 THEN 350
330 X=RND(3)
340 ON X GOTO 940,980,1020
350 IF S<>V THEN 380
360 IF Z=1 THEN 410
370 Q=1: GOTO 390
380 IF W(R,S+1)<>0 THEN 410
390 X=RND(3)
400 ON X GOTO 940,980,1090
410 X=RND(2)
420 ON X GOTO 940,980
430 IF R=H THEN 530
440 IF W(R+1,S)<>0 THEN 530
450 IF S<>V THEN 480
460 IF Z=1 THEN 510
470 Q=1: GOTO 490
480 IF W(R,S+1)<>0 THEN 510
490 X=RND(3)
500 ON X GOTO 940,1020,1090
510 X=RND(2)
520 ON X GOTO 940,1020
530 IF S<>V THEN 560
540 IF Z=1 THEN 590
550 Q=1: GOTO 570
560 IF W(R,S+1)<>0 THEN 590
570 X=INT(RND(0)*2+1)
580 ON X GOTO 940,1090
590 GOTO 940
600 IF S-1=0 THEN 790
610 IF W(R,S-1)<>0 THEN 790
620 IF R=H THEN 720
630 IF W(R+1,S)<>0 THEN 720
640 IF S<>V THEN 670
650 IF Z=1 THEN 700
660 Q=1: GOTO 680
670 IF W(R,S+1)<>0 THEN 700
680 X=RND(3)
690 ON X GOTO 980,1020,1090
700 X=RND(2)
710 ON X GOTO 980,1020
720 IF S<>V THEN 750
730 IF Z=1 THEN 780
740 Q=1: GOTO 760
750 IF W(R,S+1)<>0 THEN 780
760 X=RND(2)
770 ON X GOTO 980,1090
780 GOTO 980
790 IF R=H THEN 880
800 IF W(R+1,S)<>0 THEN 880
810 IF S<>V THEN 840
820 IF Z=1 THEN 870
830 Q=1: GOTO 990
840 IF W(R,S+1)<>0 THEN 870
850 X=RND(2)
860 ON X GOTO 1020,1090
870 GOTO 1020
880 IF S<>V THEN 910
890 IF Z=1 THEN 930
900 Q=1: GOTO 920
910 IF W(R,S+1)<>0 THEN 930
920 GOTO 1090
930 GOTO 1190
940 W(R-1,S)=C
950 C=C+1: V(R-1,S)=2: R=R-1
960 IF C=H*V+1 THEN 1200
970 Q=0: GOTO 270
980 W(R,S-1)=C
990 C=C+1
1000 V(R,S-1)=1: S=S-1: IF C=H*V+1 THEN 1200
1010 Q=0: GOTO 270
1020 W(R+1,S)=C
1030 C=C+1: IF V(R,S)=0 THEN 1050
1040 V(R,S)=3: GOTO 1060
1050 V(R,S)=2
1060 R=R+1
1070 IF C=H*V+1 THEN 1200
1080 GOTO 600
1090 IF Q=1 THEN 1150
1100 W(R,S+1)=C: C=C+1: IF V(R,S)=0 THEN 1120
1110 V(R,S)=3: GOTO 1130
1120 V(R,S)=1
1130 S=S+1: IF C=V*H+1 THEN 1200
1140 GOTO 270
1150 Z=1
1160 IF V(R,S)=0 THEN 1180
1170 V(R,S)=3: Q=0: GOTO 1190
1180 V(R,S)=1: Q=0: R=1: S=1: GOTO 260
1190 GOTO 210
1200 FOR J=1 TO V
1210 LPRINT "I";
1220 FOR I=1 TO H
1230 IF V(I,J)<2 THEN 1260
1240 LPRINT "   ";
1250 GOTO 1270
1260 LPRINT "  I";
1270 NEXT I
1280 LPRINT " "
1290 FOR I=1 TO H
1300 IF V(I,J)=0 THEN 1340
1310 IF V(I,J)=2 THEN 1340
1320 LPRINT ":  ";
1330 GOTO 1350
1340 LPRINT ":--";
1350 NEXT I
1360 LPRINT ":"
1370 NEXT J
1380 END