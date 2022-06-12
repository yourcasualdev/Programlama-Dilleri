# Taş-kağıt-makas
# Kodunuzu bu dosya içine yazınız
=begin
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
gets.chomp
yeterli...
=end

def f(n)
    if(n % 2 == 0)
        return n/2
    end
    return 3*n + 1
end

def collatz(num)

    if(num == 0)
        return 0
    end
    
    count = 0

    while(num > 1)
        count = count + 1
        num = f(num)
    end
    return count
end

input = gets.chomp.to_i
puts(collatz(input))