---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund manager
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of the party responsible for making investment decisions and managing the portfolio of an investment fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund manager is an individual or entity that oversees the investment strategy and asset allocation of a fund,
      with the objective of achieving financial returns in accordance with the fund's mandate. The fund manager may operate
      under regulatory oversight and fiduciary obligations, and may be supported by analysts, traders, and compliance officers.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund manager, often a mutual fund company, a brokerage firm, an investment adviser, or an insurance company,
      handles all of the transactions and investments within the plan.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: plan manager
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: program manager
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.investor.gov/introduction-investing/investing-basics/glossary/529-plan-or-program-manager
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundManager
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund manager
type: Ontology Class
---

# fund manager

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundManager>

## Definition

role of the party responsible for making investment decisions and managing the portfolio of an investment fund

## Relationships

- **See also**: [529-plan-or-program-manager](<https://www.investor.gov/introduction-investing/investing-basics/glossary/529-plan-or-program-manager>)
- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Annotations

- **label** (en): fund manager
- **definition** (en): role of the party responsible for making investment decisions and managing the portfolio of an investment fund
- **explanatoryNote** (en): A fund manager is an individual or entity that oversees the investment strategy and asset allocation of a fund, with the objective of achieving financial returns in accordance with the fund's mandate. The fund manager may operate under regulatory oversight and fiduciary obligations, and may be supported by analysts, traders, and compliance officers.
- **explanatoryNote** (en): A fund manager, often a mutual fund company, a brokerage firm, an investment adviser, or an insurance company, handles all of the transactions and investments within the plan.
- **synonym** (en): plan manager
- **synonym** (en): program manager

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
