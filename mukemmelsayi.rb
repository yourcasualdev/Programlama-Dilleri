# Taş-kağıt-makas
# Kodunuzu bu dosya içine yazınız
=begin
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
gets.chomp
yeterli...
=end

def isPerfect(num)
    sum = 0
    for i in 1..(num - 1)
        if(num % i == 0)
            sum += i
        end
    end
    if sum == num
        return "mükemmel"
    end
    return "mükemmel değil"
end

input = gets.chomp.to_i
puts(isPerfect(input))