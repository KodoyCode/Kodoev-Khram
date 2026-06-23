import random
import time
import sys
import msvcrt

dareje = 1
imkaniyatlar = 1
waqit = 10 

print(f"Harbir sorawga {waqit} sekund waqit beriledi.\n")

def get_answer_with_timer(timeout):
    start_time = time.time()
    user_input = ""

    sys.stdout.write(f"\r[Waqit qaldi: {timeout}s] | [Qalgan urinislar: {imkaniyatlar}] -> Juwabiniz: ")
    sys.stdout.flush()

    while True:
        elapsed = time.time() - start_time
        remaining = int(timeout - elapsed)
        
        if remaining <= 0:
            return None, elapsed 

        sys.stdout.write(f"\r[Waqit qaldi: {remaining}s] | [Qalgan urinislar: {imkaniyatlar}] -> Juwabiniz: {user_input}")
        sys.stdout.flush()
        
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            
            if char == '\r' or char == '\n':
                break
            elif char == '\b' or char == '\x08':
                if len(user_input) > 0:
                    user_input = user_input[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            elif char.isdigit() or char == '-':
                user_input += char
                
        time.sleep(0.05)
        
    return user_input, (time.time() - start_time)

while imkaniyatlar > 0:
    maksimal_shegara = 5 * dareje    
    san1 = random.randint(2, maksimal_shegara)
    san2 = random.randint(2, maksimal_shegara)
    duris_juwap = san1 * san2
    
    print(f"\n--- {dareje}-Dareje ---")
    print(f"Misal: {san1} x {san2} = ?")
    
    juwap_jaziw, ketken_waqit = get_answer_with_timer(waqit)
    ketken_waqit = round(ketken_waqit, 1)

    if juwap_jaziw is None:
        imkaniyatlar -= 1
        print(f"\n\nWaqit juwmaqlandi! {ketken_waqit} sekund waqit ketti (Shegara: {waqit}s). 1 ta imkaniyatdan ayrildingiz.")
        print(f"Duris juwap: {duris_juwap} edi.")
        if imkaniyatlar > 0:
            print(f"Qalgan urinislar sani: {imkaniyatlar}")
        continue

    juwap_jaziw = juwap_jaziw.strip()

    if not juwap_jaziw or juwap_jaziw == "-":
        imkaniyatlar -= 1
        print(f"\nJuwap kiritilmedi yaki qate! 1 imkaniyatdan ayrildingiz.")
        print(f"Duris juwap: {duris_juwap} edi.")
        if imkaniyatlar > 0:
            print(f"Qalgan urinislar sani: {imkaniyatlar}")
        continue
        
    try:
        juwap = int(juwap_jaziw)
    except ValueError:
        imkaniyatlar -= 1
        print(f"\nIltimas, tek san jazin! Qate kiritkeniniz ushin 1 imkaniyatdan ayrildingiz.")
        print(f"Duris juwap: {duris_juwap} edi.")
        if imkaniyatlar > 0:
            print(f"Qalgan urinislar sani: {imkaniyatlar}")
        continue
    

    if juwap == duris_juwap:
        qalgan_waqit = round(waqit - ketken_waqit, 1)
        print(f"\nQutliqlayman! Juwabingiz duris. Ketken waqt: {ketken_waqit}s (Qaldi: {max(0.0, qalgan_waqit)}s)")
        print("Kiyingi darejege ottiniz")
        dareje += 1
        
    else:
        imkaniyatlar -= 1
        print(f"\nQate! Duris juwap: {duris_juwap} edi. Ketken waqt: {ketken_waqit}s")
        if imkaniyatlar > 0:
            print(f"Qalgan urinislar sani: {imkaniyatlar}")

print("\n--- OYIN JUWMAQLANDI ---")
print(f"Siz {dareje}-darejege deyin jetip keldingiz.")