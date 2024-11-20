BEGIN {
  maxcal = 0;
  maxelfid = 0;
  curcal = 0
  curelfid = 1;
}

/^$/ {
  if (curcal >= maxcal) {
    # print "New max " curcal " for elf " curelfid */
    maxcal = curcal;
    maxelfid = curelfid;
  }
  curelfid = curelfid + 1;
  curcal = 0
}
/[0-9]*/ {
  curcal = curcal + $0
}

END {
  print "============DAY 01==========="
  print "Max cal " maxcal " for elf " maxelfid
  print "============================="
}
