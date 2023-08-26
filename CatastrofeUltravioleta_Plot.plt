set title "T=h/k_B"
set xlabel "{/Symbol n}(s^{-1})"
set ylabel "u({/Symbol n},T) (J{/Symbol \327}s/m^3)"

pi=3.14159
c=299792458
k=1.38*10**-23
h=6.626*10**-34


T=h/k
RJ(x)=8*pi*x**2/c**3*k*T
Wien(x)=8*pi*h/c**3*x**3*exp(-h*x/k/T)
Planck(x)=8*pi*x**3*h/c**3/(exp(h*x/k/T)-1)


set xrange [0:20]
set yrange [0:10**-57]

plot Planck(x) lc "dark-violet",Wien(x) dashtype 4 lc "dark-green",[0:2] RJ(x) title "Rayleigh-Jeans" dashtype 4 lc "medium-blue"