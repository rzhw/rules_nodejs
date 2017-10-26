load("//internal:node.bzl", "nodejs_test")
load("//internal:devmode_js_sources.bzl", "devmode_js_sources")

def jasmine_node_test(name, srcs = [], data = [], deps = [], **kwargs):
  devmode_js_sources(
      name = "%s_devmode_srcs" % name,
      deps = srcs + deps,
      testonly = 1,
  )

  runner_js = "@build_bazel_rules_nodejs//internal:jasmine_runner.js"
  all_data = data + srcs + deps + [
      runner_js,
      ":%s_devmode_srcs.MF" % name,
  ]

  nodejs_test(
      name = name,
      data = all_data,
      entry_point = "$(location %s)" % runner_js,
      templated_args = ["$(location :%s_devmode_srcs.MF)" % name],
      testonly = 1,
      **kwargs
  )
