import sys

print(sys.version)
print()

summe=0
for feld in range(64):
    reiskorn=2**feld
    summe+=reiskorn
    if reiskorn==1:
        print(f"Feld {feld+1}: {reiskorn:,.0f} Reiskorn und damit gesamt {summe:,.0f} Reiskörner")
    else:
        print(f"Feld {feld+1}: {reiskorn:,.0f} Reiskörner und damit gesamt {summe:,.0f} Reiskörner")
    vol=summe /(1e6**3) 

print(f"Wenn ein Reiskorn ein Volumen von 1mm3 hat, errechnen sich daraus {vol:,.1f} km3 (=Kubikkilometer)")
