def temperature_sortie(T_ed, T_em, c_ed, c_em, efficacite): # calcul la température de l'eau douce en sortie d'échangeur
    return efficacite*(c_em*T_em + c_ed*T_ed)/(c_ed+c_em)

def puissance_chaleur_sortie_pac(P_el, T_ed, T_em, c_ed, c_em, D_m): # calcul de la puissance thermique de sortie d'une pompe à chaleur
    return P_el+c_ed*D_m*temperature_sortie(T_ed, T_em, c_ed, c_em)

def puissance_perdue_clim(P_el, T_ed, T_em, c_ed, c_em, D_m): # calcul de la puissance thermique perdue par le bâti en fonctionnement clim
    return c_ed*D_m*temperature_sortie(T_ed, T_em, c_ed, c_em) - P_el





