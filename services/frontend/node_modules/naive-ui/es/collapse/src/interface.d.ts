export declare type OnUpdateExpandedNames = <T extends string[] & number[] & Array<string | number> & (string | number | null) & (string | null) & (number | null)>(value: T) => void;
export declare type OnUpdateExpandedNamesImpl = <T extends string[] | number[] | Array<string | number> | (string | number | null) | (string | null) | (number | null)>(value: T) => void;
export declare type OnItemHeaderClick = <T extends string & number & (string | number)>(info: HeaderClickInfo<T>) => void;
export declare type OnItemHeaderClickImpl = <T extends string | number | (string | number)>(info: HeaderClickInfo<T>) => void;
export interface HeaderClickInfo<T> {
    name: T;
    expanded: boolean;
    event: MouseEvent;
}
