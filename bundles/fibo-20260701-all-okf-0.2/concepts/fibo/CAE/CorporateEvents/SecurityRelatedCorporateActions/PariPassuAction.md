---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pari-passu action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that occurs when securities with different characteristics become identical in all respects
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A pari-passu event includes cases, for example, when shares with different entitlements to dividend or voting rights
      become equivalent through assimilation or pari-passu. Such an event may be scheduled in advance, for example, when shares
      resulting from a bonus may become fungible after a pre-set period of time, or may result from outside events, for example,
      merger, reorganisation, issue of supplementary tranches, etc.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The term, pari-passu, means ''at the same rate or on an equal footing'', and in finance is used to describe situations
      where two or more assets, securities, creditors, or obligations are equally managed without preference. An example of
      pari-passu occurs during bankruptcy proceedings: When the court reaches a verdict, the court regards all creditors equally,
      and the trustee will repay them the same fractional amount as other creditors and at the same time.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: assimilation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/PariPassuAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: pari-passu action
type: Ontology Class
---

# pari-passu action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/PariPassuAction>

## Definition

corporate action that occurs when securities with different characteristics become identical in all respects

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): pari-passu action
- **definition** (en): corporate action that occurs when securities with different characteristics become identical in all respects
- **explanatoryNote** (en): A pari-passu event includes cases, for example, when shares with different entitlements to dividend or voting rights become equivalent through assimilation or pari-passu. Such an event may be scheduled in advance, for example, when shares resulting from a bonus may become fungible after a pre-set period of time, or may result from outside events, for example, merger, reorganisation, issue of supplementary tranches, etc.
- **explanatoryNote** (en): The term, pari-passu, means 'at the same rate or on an equal footing', and in finance is used to describe situations where two or more assets, securities, creditors, or obligations are equally managed without preference. An example of pari-passu occurs during bankruptcy proceedings: When the court reaches a verdict, the court regards all creditors equally, and the trustee will repay them the same fractional amount as other creditors and at the same time.
- **synonym** (en): assimilation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
