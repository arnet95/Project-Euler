function primes(limit)
    l = [true for i in 1:limit]
    i = 2
    while i^2 <= limit
        if l[i]
            for j = i^2:i:limit
                l[j] = false
            end
        end
        i += 1
    end
    return [i for i = 2:limit if l[i]]
end

function prime_factorisations(limit)
    l = [Dict() for i in 1:limit]
    prime_list = primes(limit)
end
