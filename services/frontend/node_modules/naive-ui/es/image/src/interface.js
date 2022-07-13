import { useTheme } from '../../_mixins';
export const imagePreviewSharedProps = Object.assign(Object.assign({}, useTheme.props), { showToolbar: { type: Boolean, default: true }, showToolbarTooltip: Boolean });
