#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-tins
Version  : 1.12.0
Release  : 13
URL      : https://rubygems.org/downloads/tins-1.12.0.gem
Source0  : https://rubygems.org/downloads/tins-1.12.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-gem_hadar
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
# Tins - Useful tools library in Ruby
## Description
Non yet.
## Badges
[![Code Climate](https://codeclimate.com/github/flori/tins.png)](https://codeclimate.com/github/flori/tins)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n tins-1.12.0
gem spec %{SOURCE0} -l --ruby > rubygem-tins.gemspec

%build
export LANG=C
gem build rubygem-tins.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
tins-1.12.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/tins-1.12.0
ruby -v -I.:lib:tests test*/test_*.rb
ruby -v -I.:lib:tests test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/tins-1.12.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/TODO
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/add_one.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/add_one.stm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/bb3.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/bb3.stm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/concatenate_compare.mtm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/concatenate_compare.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/length_difference.mtm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/length_difference.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/let.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/mail.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/minsky.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/multiply.reg
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/null_pattern.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/ones_difference-mtm.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/ones_difference-stm.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/ones_difference.mtm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/ones_difference.stm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/prefix-equals-suffix-reversed-with-infix.png
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/prefix-equals-suffix-reversed-with-infix.stm
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/recipe.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/recipe2.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/recipe_common.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/subtract.reg
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/turing-graph.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/examples/turing.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/dslkit.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/dslkit/polite.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/dslkit/rude.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/spruz.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/alias.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/annotate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/ask_and_send.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/attempt.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/bijection.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/case_predicate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/complete.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/concern.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/count_by.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/date_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/date_time_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/deep_const_get.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/deep_dup.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/dslkit.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/duration.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/extract_last_argument_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/file_binary.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/find.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/go.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/hash_symbolize_keys_recursive.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/hash_union.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/if_predicate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/implement.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/limited.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/lines_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/memoize.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/method_description.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/minimize.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/module_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/named_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/null.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/once.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/p.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/partial_application.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/proc_compose.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/proc_prelude.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/range_plus.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/require_maybe.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/responding.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/secure_write.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/sexy_singleton.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/string_byte_order_mark.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/string_camelize.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/string_underscore.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/string_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/subhash.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/terminal.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/thread_local.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/time_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/to.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/to_proc.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/token.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/uniq_by.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/unit.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/write.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/annotate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/ask_and_send.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/attempt.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/blank.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/case_predicate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/complete.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/concern.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/count_by.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/date_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/date_time_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/deep_const_get.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/deep_dup.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/dslkit.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/extract_last_argument_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/file_binary.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/full.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/hash_symbolize_keys_recursive.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/hash_union.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/if_predicate.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/implement.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/irb.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/method_description.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/named.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/null.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/p.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/partial_application.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/proc_compose.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/proc_prelude.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/range_plus.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/require_maybe.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/responding.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/secure_write.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/sexy_singleton.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/string.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/string_byte_order_mark.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/string_camelize.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/string_underscore.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/string_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/subhash.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/time_dummy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/time_freezer.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/to.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/uniq_by.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/lib/tins/xt/write.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/annotate_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/ask_and_send_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/attempt_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/bijection_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/blank_full_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/case_predicate_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/concern_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/count_by_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/date_dummy_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/date_time_dummy_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/deep_const_get_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/deep_dup_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/delegate_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/dslkit_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/duaration_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/dynamic_scope_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/extract_last_argument_options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/file_binary_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/find_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/from_module_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/go_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/hash_symbolize_keys_recursive_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/hash_union_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/if_predicate_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/implement_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/limited_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/lines_file_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/memoize_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/method_description_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/minimize_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/module_group_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/named_set_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/named_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/null_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/p_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/partial_application_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/proc_compose_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/proc_prelude_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/range_plus_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/require_maybe_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/responding_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/rotate_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/scope_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/secure_write_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/sexy_singleton_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/string_byte_order_mark_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/string_camelize_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/string_underscore_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/string_version_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/subhash_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/time_dummy_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/time_freezer_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/to_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/token_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/uniq_by_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tests/unit_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/tins-1.12.0/tins.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/tins-1.12.0.gemspec
