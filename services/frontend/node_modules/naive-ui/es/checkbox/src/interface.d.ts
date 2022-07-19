export declare type OnUpdateChecked = (value: string & number & boolean, e: MouseEvent | KeyboardEvent) => void;
export declare type OnUpdateCheckedImpl = (value: string | number | boolean, e: MouseEvent | KeyboardEvent) => void;
export interface CheckboxInst {
    focus: () => void;
    blur: () => void;
}
