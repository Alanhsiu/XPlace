#pragma once

namespace db {


class CapInfo {
    friend class Database;
public:
    CapInfo(const std::string& file);
    ~CapInfo();
};
}  // namespace db