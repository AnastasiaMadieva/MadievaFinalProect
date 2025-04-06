import requests
import allure



class SkyengApi:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        #self.taskId=taskId
        #self.data=data
        #self.search = search

    @allure.step("Просмотреть события")
    def events_api(self):
        my_body={
            'from':'2025-03-21T18:30:00+05:00',
            'till':'2025-03-21T19:00:00+05:00',
            'onlyTypes':[]
        }
        my_headers={}
        my_headers['Cookie']="token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IlRYREZ1SVdIaTV0VkhSN3VRWXh1bWEyWXFodlBHNVhxIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0Mzk1NjY2NSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzAyNjIsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iMO-vZqKD0p92sKgnMM4mvEjf59r8Q44D4JNpIqXXx6dZ2fGidFPOYTaDZ8Y9R0oSaTcrFYZW0xEsDvRWNQn669r5HxCvwbo99SoP7UcfN2yyJDibZoB3AwjSmuAS_IW_uSF5iEDctVzGrofXWb7lpP997To3WuDJus8EUppR1igsZ1IDd05wezE6tkBnE_60bkY7zepmbvPnqcotyzmOhn5ZFMRdR6fDuH3JLtxnEstskGnFHmNDdpmhptWjNufd40cIaJ10AEhXQLuj53a5gArcE7GUKsHI9sIRm_K6VRyU4i497xXYxecqZutK90ZMf4XQWMxwtolsomLeaDt0L1KOhfbSqqAVtfnaY98goCYLwf3PwYw1ubgZmHrMyMvSMDRY9YJcH92unj85Zl27WvoqJyFjYsAsTyxaBrcWD-2R2bqe1iEsaGF-7vjSE2K2m5slseQTeVXbS1Q_pbSLNaCapryWHqg_mihHo37ndG4AVz-foWrK_-Gx79-zabRGn1mGOxHRv-qVNiNTUfwlINuuHPG8P2r57kuamdSgVcV-iI9KQxZHhHsFRXMaoKQ1rxFwTpxsYHcmmH7wCnkWegMjTaL8_dz_t0oTwCSSGp9oqTbjsPqQBbfPQCdWrTbq19vLDW0UIqBvVfqS0ix7J3Bmdhaiv-zfeluZz19giY"
        resp = requests.post(self.base_url+'events', json=my_body, headers=my_headers)
        return resp.json()

    @allure.step("Добавить событие")
    def createPersonal_api(self, old_title: str, old_color: str):
        my_body={
            'backgroundColor':'#F4F5F6',
            'color':old_color,
            'description':'',
            'title':old_title,
            'startAt':'2025-03-21T18:30:00+05:00',
            'endAt':'2025-03-21T19:00:00+05:00'
        }
        my_headers={}
        my_headers['Cookie']="token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IlRYREZ1SVdIaTV0VkhSN3VRWXh1bWEyWXFodlBHNVhxIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0Mzk1NjY2NSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzAyNjIsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iMO-vZqKD0p92sKgnMM4mvEjf59r8Q44D4JNpIqXXx6dZ2fGidFPOYTaDZ8Y9R0oSaTcrFYZW0xEsDvRWNQn669r5HxCvwbo99SoP7UcfN2yyJDibZoB3AwjSmuAS_IW_uSF5iEDctVzGrofXWb7lpP997To3WuDJus8EUppR1igsZ1IDd05wezE6tkBnE_60bkY7zepmbvPnqcotyzmOhn5ZFMRdR6fDuH3JLtxnEstskGnFHmNDdpmhptWjNufd40cIaJ10AEhXQLuj53a5gArcE7GUKsHI9sIRm_K6VRyU4i497xXYxecqZutK90ZMf4XQWMxwtolsomLeaDt0L1KOhfbSqqAVtfnaY98goCYLwf3PwYw1ubgZmHrMyMvSMDRY9YJcH92unj85Zl27WvoqJyFjYsAsTyxaBrcWD-2R2bqe1iEsaGF-7vjSE2K2m5slseQTeVXbS1Q_pbSLNaCapryWHqg_mihHo37ndG4AVz-foWrK_-Gx79-zabRGn1mGOxHRv-qVNiNTUfwlINuuHPG8P2r57kuamdSgVcV-iI9KQxZHhHsFRXMaoKQ1rxFwTpxsYHcmmH7wCnkWegMjTaL8_dz_t0oTwCSSGp9oqTbjsPqQBbfPQCdWrTbq19vLDW0UIqBvVfqS0ix7J3Bmdhaiv-zfeluZz19giY"
        resp = requests.post(self.base_url+'createPersonal',json=my_body, headers=my_headers)
        return resp.json()   

    @allure.step("Удалить событие ")
    def removePersonal_api(self, taskId: int):
        my_body={
            'id':taskId,
            'startAt':'2025-03-21T18:30:00+05:00'
        }
        my_headers={}
        my_headers['Cookie']="token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IlRYREZ1SVdIaTV0VkhSN3VRWXh1bWEyWXFodlBHNVhxIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0Mzk1NjY2NSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzAyNjIsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iMO-vZqKD0p92sKgnMM4mvEjf59r8Q44D4JNpIqXXx6dZ2fGidFPOYTaDZ8Y9R0oSaTcrFYZW0xEsDvRWNQn669r5HxCvwbo99SoP7UcfN2yyJDibZoB3AwjSmuAS_IW_uSF5iEDctVzGrofXWb7lpP997To3WuDJus8EUppR1igsZ1IDd05wezE6tkBnE_60bkY7zepmbvPnqcotyzmOhn5ZFMRdR6fDuH3JLtxnEstskGnFHmNDdpmhptWjNufd40cIaJ10AEhXQLuj53a5gArcE7GUKsHI9sIRm_K6VRyU4i497xXYxecqZutK90ZMf4XQWMxwtolsomLeaDt0L1KOhfbSqqAVtfnaY98goCYLwf3PwYw1ubgZmHrMyMvSMDRY9YJcH92unj85Zl27WvoqJyFjYsAsTyxaBrcWD-2R2bqe1iEsaGF-7vjSE2K2m5slseQTeVXbS1Q_pbSLNaCapryWHqg_mihHo37ndG4AVz-foWrK_-Gx79-zabRGn1mGOxHRv-qVNiNTUfwlINuuHPG8P2r57kuamdSgVcV-iI9KQxZHhHsFRXMaoKQ1rxFwTpxsYHcmmH7wCnkWegMjTaL8_dz_t0oTwCSSGp9oqTbjsPqQBbfPQCdWrTbq19vLDW0UIqBvVfqS0ix7J3Bmdhaiv-zfeluZz19giY"
        resp = requests.post(self.base_url+'removePersonal', json=my_body, headers=my_headers)
        return resp.json()   
    

    @allure.step("Редактировать название события ")
    def updatePersonal_title_api(self, taskId: int, new_title: str):
        my_body={

            'backgroundColor':'#F4F5F6',
            'color':'#81888D',
            'description':'',
            'title':new_title,
            'startAt':'2025-03-21T18:30:00+05:00',
            'endAt':'2025-03-21T19:00:00+05:00',
            'id':taskId,
            'oldStartAt':'2025-03-21T18:30:00+05:00'             
        }
        my_headers={}
        my_headers['Cookie']="token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IlRYREZ1SVdIaTV0VkhSN3VRWXh1bWEyWXFodlBHNVhxIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0Mzk1NjY2NSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzAyNjIsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iMO-vZqKD0p92sKgnMM4mvEjf59r8Q44D4JNpIqXXx6dZ2fGidFPOYTaDZ8Y9R0oSaTcrFYZW0xEsDvRWNQn669r5HxCvwbo99SoP7UcfN2yyJDibZoB3AwjSmuAS_IW_uSF5iEDctVzGrofXWb7lpP997To3WuDJus8EUppR1igsZ1IDd05wezE6tkBnE_60bkY7zepmbvPnqcotyzmOhn5ZFMRdR6fDuH3JLtxnEstskGnFHmNDdpmhptWjNufd40cIaJ10AEhXQLuj53a5gArcE7GUKsHI9sIRm_K6VRyU4i497xXYxecqZutK90ZMf4XQWMxwtolsomLeaDt0L1KOhfbSqqAVtfnaY98goCYLwf3PwYw1ubgZmHrMyMvSMDRY9YJcH92unj85Zl27WvoqJyFjYsAsTyxaBrcWD-2R2bqe1iEsaGF-7vjSE2K2m5slseQTeVXbS1Q_pbSLNaCapryWHqg_mihHo37ndG4AVz-foWrK_-Gx79-zabRGn1mGOxHRv-qVNiNTUfwlINuuHPG8P2r57kuamdSgVcV-iI9KQxZHhHsFRXMaoKQ1rxFwTpxsYHcmmH7wCnkWegMjTaL8_dz_t0oTwCSSGp9oqTbjsPqQBbfPQCdWrTbq19vLDW0UIqBvVfqS0ix7J3Bmdhaiv-zfeluZz19giY"
        resp = requests.post(self.base_url+'updatePersonal', json=my_body, headers=my_headers)
        return resp.json()   
    

    @allure.step("Редактировать цвет события ")
    def updatePersonal_color_api(self, taskId: int, new_color: str):
        my_body={

            'backgroundColor':'#F4F5F6',
            'color':new_color,
            'description':'',
            'title':'Личное событие',
            'startAt':'2025-03-21T18:30:00+05:00',
            'endAt':'2025-03-21T19:00:00+05:00',
            'id':taskId,
            'oldStartAt':'2025-03-21T18:30:00+05:00'             
        }
        my_headers={}
        my_headers['Cookie']="token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6IlRYREZ1SVdIaTV0VkhSN3VRWXh1bWEyWXFodlBHNVhxIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0Mzk1NjY2NSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzAyNjIsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.iMO-vZqKD0p92sKgnMM4mvEjf59r8Q44D4JNpIqXXx6dZ2fGidFPOYTaDZ8Y9R0oSaTcrFYZW0xEsDvRWNQn669r5HxCvwbo99SoP7UcfN2yyJDibZoB3AwjSmuAS_IW_uSF5iEDctVzGrofXWb7lpP997To3WuDJus8EUppR1igsZ1IDd05wezE6tkBnE_60bkY7zepmbvPnqcotyzmOhn5ZFMRdR6fDuH3JLtxnEstskGnFHmNDdpmhptWjNufd40cIaJ10AEhXQLuj53a5gArcE7GUKsHI9sIRm_K6VRyU4i497xXYxecqZutK90ZMf4XQWMxwtolsomLeaDt0L1KOhfbSqqAVtfnaY98goCYLwf3PwYw1ubgZmHrMyMvSMDRY9YJcH92unj85Zl27WvoqJyFjYsAsTyxaBrcWD-2R2bqe1iEsaGF-7vjSE2K2m5slseQTeVXbS1Q_pbSLNaCapryWHqg_mihHo37ndG4AVz-foWrK_-Gx79-zabRGn1mGOxHRv-qVNiNTUfwlINuuHPG8P2r57kuamdSgVcV-iI9KQxZHhHsFRXMaoKQ1rxFwTpxsYHcmmH7wCnkWegMjTaL8_dz_t0oTwCSSGp9oqTbjsPqQBbfPQCdWrTbq19vLDW0UIqBvVfqS0ix7J3Bmdhaiv-zfeluZz19giY"
        resp = requests.post(self.base_url+'updatePersonal', json=my_body, headers=my_headers)
        return resp.json()   