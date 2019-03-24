<?php

if (isset($_POST["encoding_string"])) {
    $encoded_string = $_POST["encoding_string"];
    $image_name     = $_POST["image_name"];
    $decoded_string = base64_decode($encoded_string);
    $file           = fopen($image_name, 'wb');
    $is_written     = fwrite($file, $decoded_string);
    fclose($file);
	$path           = "/images/".$image_name;
    if ($is_written > 0) {
        $connection = mysqli_connect('127.0.0.1:3306', 'root', '', 'images');
        $query      = mysqli_prepare($connection, "INSERT INTO photos(name,path) values(?,?)");
		mysqli_stmt_bind_param($query,"ss", $image_name, $path);
        $result     = mysqli_stmt_execute($query);
        if ($result) {
            echo "success";
        } else {
            echo "failed1";
        }
        mysqli_close($connection);
    } else {
        echo "failed2";
    }
}

?>