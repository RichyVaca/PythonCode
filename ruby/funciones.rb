def mensaje()
    return "hola"
end

def suma(n1,n2)
    return n1+n2
end

def resta(n1,n2)
    return n1-n2
end

def producto(n1,n2)
    return n1*n2
end

def division(n1,n2)
    return Floar(n1)/Float(n2)
end

def compara(n1,n2)
    if n1>n2
        puts  "#{n1} es mayor que #{2}"
    elsif n2>n1
        puts  "#{n1} es mayor que #{2}"
    else
        puts "Los numeros son iguales: #{n1} , #{n2}"
    end
end

def cuenta(n1,n2)
    if n1>n2
        (n1..n2).each do |i|
            puts "Elemento :", i
        end
    elsif n2>n1
        while n1>n2
            puts "Elemento :", i
            n2++
        end
    else
        puts "Los numeros son iguales: #{n1} , #{n2}"
    end
ciclo = "S"
while (ciclo == "s" || ciclo == "S")

print "--- Operaciones Basicas con Ruby ---"

print "Introduce el primer numero: \n"
n1 = Integer(gets.chomp) 

print "Introduce el segundo numero: \n"
n2 = Integer(gets.chomp)



print mensaje()+"\n"
print "La suma es: ", suma(n1,n2), "\n"
print "La resta es: ", resta(n1,n2), "\n"
print "La multiplicación es: ", producto(n1,n2), "\n"
print "La division es: ", division(n1,n2), "\n"

compara(n1,n2)
cuenta(n1,n2)

puts "¿desea otra operacion? S/N"
ciclo = get.chomp

end

puts "*** FIn de programa"
