from db.models.User import User, BioVector, Prompt
from db.user_rep import UserRepository
from widgets.MSG import MSG


class Metric:
    def __init__(self):
        self.press_time = []
        self.release_time = []


class Biometric:
    TO_LIMIT = 3000

    def __init__(self):
        self.current_metric = self.get_new_metric()
        self.user_rep = UserRepository()

    def get_new_metric(self):
        return Metric()

    def submit_metric(self, username, password):
        self.filter_metric()

        biovector = BioVector(
            input_time=", ".join(map(str, self.current_metric.release_time)),
            hold_time=", ".join(map(str, self.current_metric.press_time))
        )

        existing_user = self.user_rep.get_user_by_name(username)

        if not existing_user:
            user = User(
                name=username,
                password=password
            )

            user.biovectors.append(biovector)

            self.user_rep.add_user(user)

            MSG("Уведомление", "Добавлен пользователь")
        elif existing_user.password == password:
            self.user_rep.add_bio_to_user(username, biovector)

            MSG("Уведомление", "Добавлен вектор")
        else:
            MSG("Уведомление", "Пользователь существует")

    def filter_metric(self):
        result_metric = Metric()
        for v_idx in range(len(self.current_metric.press_time)):
            if self.current_metric.press_time[v_idx] < self.TO_LIMIT \
                    and self.current_metric.release_time[v_idx] < self.TO_LIMIT:
                result_metric.press_time.append(self.current_metric.press_time[v_idx])
                result_metric.release_time.append(self.current_metric.release_time[v_idx])

        self.current_metric = result_metric

    def auth(self, username, password):
        user = self.user_rep.find_user(username, password)
        if not user:
            MSG("Уведомление", "Пользователь не найден")
        else:
            raw_vectors = self.user_rep.get_vectors_of_user(user)
            if len(raw_vectors) == 0:
                MSG("Уведомление", "Нет биометрической информации")
            else:
                vectors = []
                for v in raw_vectors:
                    m = Metric()
                    m.release_time = list(map(int, v.input_time.split(", ")))
                    m.press_time = list(map(int, v.hold_time.split(", ")))
                    vectors.append(m)

                target = "release_time" # change 4 different metric

                mins = self.find_agg(vectors, target, min)
                maxes = self.find_agg(vectors, target, max)

                data = self.pack_data(mins, maxes)

                prompt = Prompt(
                    user_id=user.id,
                    data=", ".join(map(str, data))
                )

                self.user_rep.post_prompt(prompt)

                hamming_vector = [1 if min_max[0] <= self.get_target_metric(target)[i] <= min_max[1] else 0 for i, min_max in
                                  enumerate(zip(mins, maxes))]

                if hamming_vector.count(1) >= .6 * len(hamming_vector):
                    MSG("Уведомление", "Аутентификация успешна")
                else:
                    MSG('Уведомление', 'Аутентификация провалена')

    def find_agg(self, vecs, target, func):
        res = []
        for v in vecs:
            res.append(func(v.__getattribute__(target)))
        return res

    def pack_data(self, mins, maxes):
        v = []
        for i in range(len(mins)):
            v.append(mins[i])
            v.append(maxes[i])
        return v

    def get_target_metric(self, target):
        return self.current_metric.__getattribute__(target)