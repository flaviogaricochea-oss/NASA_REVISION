import math

def calcular_orbita_real():
    mu = 3.986004418e14  
    R_EQUATORIAL = 6378137.0  
    J2 = 1.08262668e-3  
    altitude_iss = 408000.0  
    r = R_EQUATORIAL + altitude_iss
    
    v_newton = math.sqrt(mu / r)
    fator_correcao = (3/2) * J2 * (R_EQUATORIAL / r)**2 * (1.5 * (math.sin(math.radians(51.6))**2) - 0.5)
    
    v_final_ms = v_newton * (1 + fator_correcao)
    v_final_kmh = v_final_ms * 3.6

    print(f"--- PROTOCOLO NASA: ACERTO DE CONTAS ---")
    print(f"ARQUITETO: FLAVIO GARICOCHEA")
    print(f"VELOCIDADE REAL CALCULADA: {v_final_kmh:.6f} km/h")
    print(f"ASS: FLAVIO GARICOCHEA")

if __name__ == "__main__":
    calcular_orbita_real()
