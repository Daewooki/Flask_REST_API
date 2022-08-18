from flask import Flask, request, jsonify

app = Flask(__name__)

# employees

employees = [
    {
        "name": "대세",
        "id": "2022081801",
        "age": 29,
        "work": "ML Engineer",
        "team": "AI Dev"
    },
    {
        "name": "대오",
        "id": "2022081802",
        "age": 30,
        "work": "UI/UX Designer",
        "team": "AI Dev"
    },
    {
        "name": "대육",
        "id": "2022081803",
        "age": 31,
        "work": "DevOps",
        "team": "Infra"
    },
    {
        "name": "대팔",
        "id": "2022081804",
        "age": 32,
        "work": "MLOps",
        "team": "Infra"
    },
    {
        "name": "대영",
        "id": "2022081805",
        "age": 33,
        "work": "Data Engineer",
        "team": "Data Dev"
    }
]

# 모든 직원 정보 조회
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({'employees': employees})

# ID로 직원 정보 조회
@app.route('/employees/<string:id>', methods=['GET'])
def get_employees_with_id(id):
    for emp in employees:
        if id==emp['id']:
            return jsonify({'employees': emp})
    return jsonify({'employees': '일치 직원 없음'})

# 신규 직원 정보 추가
@app.route('/new_employees', methods=['POST'])
def new_employees():
    if request.method == 'POST':
        params = request.get_json()
        temp = {}
        temp['name'] = params['name']
        temp['id'] = params['id']
        temp['age'] = params['age']
        temp['work'] = params['work']
        temp['team'] = params['team']
        employees.append(temp)
        return jsonify({'New': temp}), 201

# ID로 직원 정보 업데이트
@app.route('/employees/<string:id>', methods=['PUT'])
def update_employees(id):
    params = request.get_json()
    for emp in employees:
        if id==emp['id']:
            temp = emp
            temp['team'] = params['team']
            emp = temp
            return jsonify({'update': temp})
    return jsonify({'update': '일치 직원 없음'})

# ID로 직원 정보 삭제
@app.route('/employees/<string:id>',methods=['DELETE'])
def delete_employees(id):
    for emp in employees:
        print(employees)
        if id==emp['id']:
            employees.remove(emp)
            print(employees)
            return jsonify({'delete': True})
    return jsonify({'delete': '일치 직원 없음'})

if __name__ == '__main__':
	app.run(host='0.0.0.0')