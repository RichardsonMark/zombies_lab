from db.run_sql import run_sql
from models.biting import Biting
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

def save(biting):
  sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
  values = [biting.human.id, biting.zombie.id]
  results = run_sql(sql, values)
  id = results[0]['id']
  biting.id = id


def select_all():
  bitings = []
  sql = "SELECT * FROM bitings"
  results = run_sql(sql)
  for result in results:
    human = human_repository.select(result['human_id'])
    zombie = zombie_repository.select(result['zombie_id'])
    biting = Biting(human, zombie, result['id'])
    bitings.append(biting)
  return bitings

def select(id):
  biting = None
  sql = "SELECT * FROM bitings WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  if result is not None:
    biting = Biting(result['human_id'], result['zombie_id'],result['id'])
  return biting
