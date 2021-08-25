from unittest.mock import MagicMock


class TestCart:

    def setup_method(self) -> None:
        pass

    def test_products_initially_empty(self):
        # badamy czy zanim dodamy produkty do listy jest ona pusta tzn. nie musimy używać mockowania, ponieważ nic nie
        # dodajemy
        pass

    def test_add_products(self):
        # przetestujmy metode add_product() na dwóch mockach produktów (na dwóch obiektach MagicMock)
        # chcemy najpierw dodać te obiekty do koszyka po czym sprawdzić czy get_product() zwróci nam listę mocków,
        # które dodaliśmy.
        # Dla uproszczenia w pierwszym przykładzie stworzono juz mocki produktów oraz wartość oczekiwaną
        first_mock = MagicMock()
        second_mock = MagicMock()

    def test_get_products_number(self):
        # przetestujmy czy gdy dodamy dwa produkty do koszyka czy get_products_number zwróci nam 2
        # tym razem nalezy samemu stworzyc mocki produktow, warto sugerowac sie poprzednim przykladem
        pass

    def test_compute_sum(self):
        # chcemy przetestowac czy wartosc zwracana przez metodę compute_sum() jest równa sumie cen dodanych produktów.
        # w tym celu musimy stworzyć atrapy produktów posiadające określoną wartość zwracaną przy wywołaniu metody
        # get_price() na produkcie.
        # Dla uproszczenia pierwszy mock został już stworzony. Należy stworzyć drugi mock z inną ceną (wartością
        # zwracaną).
        # Chcemy takze przetestować czy metoda get_price została wywołana na każdym z produktów. Do tego celu należy
        # użyć specjalnych asercji mocków. Np. metoda assert_called_once() wywołana na rzecz mocka metody get_price().
        first_mock = MagicMock()
        first_mock.get_price.return_value = 5
