BEGIN {
  curelfid = 0;
}

/^$/ {
  curelfid = curelfid + 1;
}
/[0-9]*/ {
  cal[curelfid] = cal[curelfid] + $0
}

END {
  asort(cal)
  curelfid = curelfid + 1
  #print cal[curelfid]
  #print cal[curelfid - 1]
  #print cal[curelfid - 2]

  maxcal = cal[curelfid] + cal[curelfid - 1] + cal[curelfid - 2]
  print "============DAY 01b=========="
  print "Max cal " maxcal
  print "============================="
}
