torn=c();for (i in 1000:9999) { if (i==((i%/%100)+(i%%100))^2 && length(table(strsplit(toString(i),"")))==4) torn<-c(torn,i) }; print(torn)
