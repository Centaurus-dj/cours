# !usr/bin/env python3
# -*- utf-8 -*-

### Format de la journée: jj/mm/aaaa ou jour mois année

def check(entry: list, type: int):
  global liste_mois
  status = False

  if len(entry) == 3:
    if type == 0:
      if len(entry[0]) == 2:
        status = True
      else:
        status = False

      if len(entry[1]) == 2:
        status = True
      else:
        status = False

    else:
      if len(entry[0]) == 2:
        status = True
      else:
        status = False

      if len(entry[1]) in set(liste_mois):
        status = True
      else:
        status = False
  else:
    raise Exception("FormatError: La date donnée n'est pas dans un format supporté")

  if len(entry[2]) > 0:
    status = True
  else:
    status = False

  return status

def isBisextile(annee):
  if type(annee) is int:
    if (annee%2) == 0:
      return True
    else:
      return False

### In-Func loop steps
###
### - ajoute à liste jour
### - curr_day += 1
### - week_day += 1
### - si week_day >= 6 --> reset 0,  week_nbr += 1

def generateMonthDays(month_length: int, year: int) -> list:
  global jours_semaine
  global index_desired_date_day
  global taille_mois

  curr_day = 1
  week_day = 0
  week_nbr = 0
  month_list = []

  test_year_list = []
  test_month_list = []

  x = 1
  ### Determine change rate of one year of date of 1st January
  for i in range(0, 12):
    y = i+1
    print(y, taille_mois[y])
    for day in range(0, taille_mois[y]):
      test_month_list.append(jours_semaine[day//7 if day >= 7 else day])
      print(day//7 if day >= 7 else day)

  #for i in range(0, year):
  #  pass

  while week_nbr <= 4:
    month_list.append([curr_day, jours_semaine[week_day]])
    curr_day += 1
    week_day += 1
    if week_day >= 6:
      week_day = 0
      week_nbr += 1

  if month_list[0][1] == index_desired_date_day:
    print("Wouhou!")
  else:
    print("still not satisfying, because:")
    print(month_list[0][0], month_list[0], "-->", index_desired_date_day, desired_date)
  exit()

  return month_list

liste_mois = [
    len("janvier"),
    len("fevrier"),
    len("mars"),
    len("avril"),
    len("mai"),
    len("juin"),
    len("juillet"),
    len("aout"),
    len("septembre"),
    len("octobre"),
    len("novembre"),
    len("décembre"),
]
taille_mois = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}
jours_semaine = [
  "Lundi",
  "Mardi",
  "Mercredi",
  "Jeudi",
  "Vendredi",
  "Samedi",
  "Dimanche",
]
date_reference = "01/01/1"
index_date_reference_jour = 0
desired_date = "01/01/2021"
index_desired_date_day = 4

date_type = None
test_date = "01/01/2020"
#date = input("Entrer la date: ").strip().split("/")
date = test_date.strip().split("/")


if len(date) > 1:
  date_type = 0
else:
  date = "".join(date).split(" ")
  date_type = 1

print("Formated date:", date)

if check(date, date_type):
  if isBisextile(int(date[2])):
    taille_mois[2] = 29
    print(generateMonthDays(taille_mois[1], 2020))
  else:
    print("annee non-bi")
else:
  raise Exception("FormatError: Le format de la date n'est pas supporté")
