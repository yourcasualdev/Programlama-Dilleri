# Taş-kağıt-makas
# Kodunuzu bu dosya içine yazınız
=begin
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
gets.chomp
yeterli...
=end

input1 = gets.chomp
input2 = gets.chomp


def game(input1, input2)
    if input1 == input2
        return "berabere"
    end
    if input1 == "taş" && input2 == "kağıt"
        return "ikinci oyuncu kazandı"
    end
    if input1 == "taş" && input2 == "makas"
        return "birinci oyuncu kazandı"
    end
    if input1 == "makas" && input2 == "kağıt"
        return "birinci oyuncu kazandı"
    end
    if input1 == "makas" && input2 == "taş"
        return "ikinci oyuncu kazandı"
    end
    if input1 == "kağıt" && input2 == "makas"
        return "ikinci oyuncu kazandı"
    end
    if input1 == "kağıt" && input2 == "taş"
        return "birinci oyuncu kazandı"
    end
end


puts game(input1, input2)