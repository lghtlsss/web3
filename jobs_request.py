from data.jobs import Jobs


def get_jobs(session):
    res = []
    for work in session.query(Jobs).all():
        res.append(
            [work.id, work.job, work.team_leader, f'{work.work_size} hours', work.collaborators, work.is_finished])
    return res
