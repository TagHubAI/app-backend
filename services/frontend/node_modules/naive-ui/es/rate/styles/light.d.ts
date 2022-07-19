import type { ThemeCommonVars } from '../../_styles/common';
import { Theme } from '../../_mixins';
declare const self: (vars: ThemeCommonVars) => {
    itemColor: string;
    itemColorActive: string;
    sizeSmall: string;
    sizeMedium: string;
    sizeLarge: string;
};
export declare type RateThemeVars = ReturnType<typeof self>;
declare const themeLight: Theme<'Rate', RateThemeVars>;
export default themeLight;
export declare type RateTheme = typeof themeLight;
