---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: packaged financial product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial product that acts as a container for at least one financial instrument, including other financial products,
      and whose value is derived from, or based on a reference asset, market measure, or investment strategy
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: 'Packaged products are typically included in an institution''s approved product catalog, i.e., pre-approved by
      compliance organizations for sale to clients. Not all institutions maintain such a catalog, with internal identifiers
      for such products, but many do. Such core products may have as attributes: Type (product and possibly asset class),
      product identifier, status and approval date, product family approval (as appropriate), and so forth.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Certain properties of the instruments, such as their term, interest rate, eligibility of the client, etc., may
      be set as a part of the product specification. Some of these are intrinsic but variable properties of the instrument,
      for example the exact interest rate, whereas others are extrinsic, such as client eligibility. Product offerings have
      prices, which may build in various fees, that are components of the cost of carry on a trader's books.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Reference assets and market measures may include single equity or debt securities, indexes, commodities, interest
      rates and/or foreign currencies, as well as baskets of these reference assets or market measures. Like other well-known
      market instruments such as convertible bonds, many structured products are hybrid securities. Structured products typically
      have two components - a debt instrument and a derivative, which is often an option. The debt instrument, in some instances,
      may pay interest at a specified rate and interval. The derivative component establishes payment at maturity, which may
      give the issuer the right to buy from you, or sell you, the referenced security or securities at a predetermined price.
      For example, structured products may combine characteristics of debt and equity or of debt and commodities.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: SEC Rule 434 defines structured securities as 'securities whose cash flow characteristics depend upon one or more
      indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's
      payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest
      rates or cash flows'.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market-linked investment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: structured product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: N45bede34f4784d56a9396b6bb01b1cb7
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/Archives/edgar/data/36995/000121465907002234/c101872fwp.htm
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ContractualProduct
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PackagedFinancialProduct
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: packaged financial product
type: Ontology Class
---

# packaged financial product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PackagedFinancialProduct>

## Definition

financial product that acts as a container for at least one financial instrument, including other financial products, and whose value is derived from, or based on a reference asset, market measure, or investment strategy

## Relationships

- **See also**: [c101872fwp.htm](<https://www.sec.gov/Archives/edgar/data/36995/000121465907002234/c101872fwp.htm>)
- **Subclass of**: [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- **Subclass of**: [ContractualProduct](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `N45bede34f4784d56a9396b6bb01b1cb7`
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: min qualified cardinality 0 of type [FinancialProductCatalog](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog.md)

## Annotations

- **label**: packaged financial product
- **definition**: financial product that acts as a container for at least one financial instrument, including other financial products, and whose value is derived from, or based on a reference asset, market measure, or investment strategy
- **scopeNote**: Packaged products are typically included in an institution's approved product catalog, i.e., pre-approved by compliance organizations for sale to clients. Not all institutions maintain such a catalog, with internal identifiers for such products, but many do. Such core products may have as attributes: Type (product and possibly asset class), product identifier, status and approval date, product family approval (as appropriate), and so forth.
- **explanatoryNote**: Certain properties of the instruments, such as their term, interest rate, eligibility of the client, etc., may be set as a part of the product specification. Some of these are intrinsic but variable properties of the instrument, for example the exact interest rate, whereas others are extrinsic, such as client eligibility. Product offerings have prices, which may build in various fees, that are components of the cost of carry on a trader's books.
- **explanatoryNote**: Reference assets and market measures may include single equity or debt securities, indexes, commodities, interest rates and/or foreign currencies, as well as baskets of these reference assets or market measures. Like other well-known market instruments such as convertible bonds, many structured products are hybrid securities. Structured products typically have two components - a debt instrument and a derivative, which is often an option. The debt instrument, in some instances, may pay interest at a specified rate and interval. The derivative component establishes payment at maturity, which may give the issuer the right to buy from you, or sell you, the referenced security or securities at a predetermined price. For example, structured products may combine characteristics of debt and equity or of debt and commodities.
- **explanatoryNote**: SEC Rule 434 defines structured securities as 'securities whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows'.
- **synonym**: market-linked investment
- **synonym**: structured product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
