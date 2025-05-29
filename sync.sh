source_dir="template-name"
target_dir="{{cookiecutter.project_slug}}"

rm -rf "${target_dir}"
cp -r "${source_dir}" "${target_dir}"

rename_srcs=("template-name" "template_name")
rename_targets=("{{cookiecutter.project_name_robot}}" "{{cookiecutter.project_slug}}")

for i in "${!rename_srcs[@]}"; do
  src="${rename_srcs[$i]}"
  tgt="${rename_targets[$i]}"
  rnr regex --recursive --include-dirs --force --no-dump "$src" "$tgt" "${target_dir}"
  grep --recursive --files-with-matches --exclude-dir=".git" "$src" "${target_dir}" | xargs sed --in-place "s/$src/$tgt/g"
done


rm -rf "${target_dir}/src/lib/richards-toolbox"