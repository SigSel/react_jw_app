install.packages("pacman")
pacman::p_load(tidyverse, writexl)

#library(tidyverse)
#library(writexl)

ads <- map(paste0("search.json"), fromJSON)
data_raw <- pluck(ads,1, "productSearchResult")
data <- pluck(data_raw, "products")

#Extract variables from the data
data_f <- data %>% 
  select(code, name, url, product_selection)#, status, buyable, inStockSupplier)

#Add price to the data, price is element two in the price list
numob <- nrow(data_f)
price <- data %>% 
  select(price)
price <- unlist(price)
price <- price[(nrow(data_f)+1):(nrow(data_f)*2)] 
data_f <- cbind(data_f, price)

#Add volume to the data, volume is the first element in volume list
volume <- data %>% 
  select(volume)
volume <- unlist(volume)
volume <- volume[1:numob] 
data_f <- cbind(data_f, volume)

im <- data %>% 
  select(images)
im <- unlist(im)
images <- array()
for (i in 1:nrow(data_f)) {
  images[i] <- im[i*6]
}
data_f <- cbind(data_f, images)

write.csv(data_f, file='../src/JW_vinmon.csv')

