<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

use Illuminate\Support\Facades\Http;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::post("/predict", "clients@predict");

Route::resources([
	'messages' => "MessageController",
]);


Route::get("/crawler/{country?}", function ($country = null) {
	$response = Http::get("http://localhost:5000/crawler?country=" . $country);
	return Response($response);
});